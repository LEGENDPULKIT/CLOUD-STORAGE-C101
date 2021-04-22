import dropbox

class TransferData:

    def __init__(self,access_token):

        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='h-9vf199QgsAAAAAAAAAAX6E0ZEyFby6z1jgp1Z28q6nNFdfTZ1rl_DePFWFujoM'

    transferdata=TransferData(access_token)

    file_from=input("Enter the file path to upload: ")
    file_to=input("Enter the full path to upload to drop box: ")

    transferdata.upload_file(file_from,file_to)
    print("File has been moved")

main()