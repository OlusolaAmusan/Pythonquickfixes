
# coding: utf-8

# In[22]:


#c = open('doc61.txt', 'w+')
#c.write ("This is amusan")
#c.close()

#This segment Appends our string to contents of a Notepad file and creates one if the file doesnt exist

c=open("drcv.txt", "a+")
c.write("Appending I am 20 Years old")
c.close()

#Then let us go on to read from our our Notepad file and appended content

c=open("drcv.txt", "r")
if c.mode =='r':  #confirm if text file is in read mode
    contents =c.read()  #Now read with the .read command
c.close()
print (contents) #Print out content

