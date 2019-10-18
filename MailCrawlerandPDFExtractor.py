#!/usr/bin/env python
# coding: utf-8

# In[3]:


import datetime
import os
import win32com.client


# In[4]:


path = os.path.expanduser("C:/Users/rajat.chaudhari/Desktop/1")
today = datetime.date.today()
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6) 
messages = inbox.Items


# In[14]:


#message.Subject == "some subject"
for message in messages:
    if  message.Attachments.Count > 0 and message.Unread:
        # body_content = message.body
        attachments = message.Attachments
        attachment = attachments.Item(1)
        for attachment in message.Attachments:
            if str(attachment).split('.')[-1]=='pdf':
                attachment.SaveAsFile(os.path.join(path, str(attachment)))
                message.Unread = False
                break


# In[15]:


import PyPDF2
# pdf file object
# you can find find the pdf file with complete code in below
pdfFileObj = open('../test invoice - Copy.pdf', 'rb')
# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# number of pages in pdf
print(pdfReader.numPages)
# a page object
pageObj = pdfReader.getPage(0)
# extracting text from page.
# this will print the text you can also save that into String
print(pageObj.extractText())


# In[ ]:




