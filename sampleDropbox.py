import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')

        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BKz98fagRCIOGs5t0ml8zhVXoQ9HDYVz_iT5D5omoVH2K2M_y1iN2rPL0EAQYIglMklCl5iQGUIGxrf4b-8OMQ-zTzqUdryBw518FzXhdhRekm_nMBHtygjPx9fj1q767AtsC3cZrxnB'
    transferData = TransferData(access_token)

    file_from ='C:/Users/Lenovo/Desktop/py/test.txt'
    file_to = '/test.txt'

    # API v2
    transferData.upload_file(file_from, file_to)
    
    print("file has been moved !!!")


main()