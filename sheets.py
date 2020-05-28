import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
import KeepEdit, exceptions

#Setup creds
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

#Open sheet as 'sheet'
sheet = client.open("Payments").sheet1

#Get reference day for calculating time until payment
today = date.today()

data = sheet.get_all_records()

#creates Keep object and logs in with given credentials
def startup():
    keepObj = KeepEdit.createKeepObject()
    if KeepEdit.loginNow(keepObj, 'brunerm99', 'fczqbrnkjmzvptut'):
        print(True)
        return keepObj
    else:
        print("BadKeepLogin")
        raise exceptions.BadKeepLogin

#creates a note with upcoming payment info
def upcomingPaymentNote(upcomingPayments):
    keepObj = startup()

    for payment in upcomingPayments:
        service, day, numDays = payment
        KeepEdit.addNote(keepObj, 'Upcoming Payment',
                         "Service: {}\nAmount: ${}\nDate: {} ({} days)".format(service['Name'], service['Amount'],
                                                                              str(day.month) + "/" + str(
                                                                                  service['Payment Date']), numDays))
        KeepEdit.update(keepObj)

#Check if payment is in next 3 days
#returns [[service1, tempDay1, numDays1], [service2.....]]
def checkPaymentDate():
    upcomingPayments = []
    for service in data:
        tempDay = date(today.year, today.month, service['Payment Date'])
        numDays = int((tempDay - today).days)
        if service['Period'] == 'Monthly' and 0 <= numDays <= 3:
            tempPayment = [service, tempDay, numDays]
            upcomingPayments.append(tempPayment)
    return upcomingPayments

def main():
    upcomingPaymentNote(checkPaymentDate())

if __name__ == '__main__':
    main()