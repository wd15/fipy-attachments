import tratihubis
import os
import wget


url = 'http://matforge.org/fipy'
attachments = '/tmp/attachments.csv'
basepath = os.path.join('raw-attachment', 'ticket')
attachmentsPrefix = os.path.join(url, basepath)

attachmentsMap = tratihubis._createTicketsToAttachmentsMap(attachments, attachmentsPrefix)

for ticketId, attachmentList in attachmentsMap.items():
    cwd = os.getcwd()
    download_to = os.path.join(basepath, str(ticketId))
    if not os.path.exists(download_to):
        os.mkdir(download_to)
    os.chdir(download_to)
    for attachmentDict in attachmentList:
        wget.download(attachmentDict['fullpath'])
    os.chdir(cwd)
        

