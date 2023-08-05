from tkinter import *

class NLPApp():
    
    def __init__(self):
        
        # login page
        self.root = Tk()
        self.root.title('NLP APP')
        self.root.iconbitmap('Resources/favicon.ico')
        self.root.geometry('480x620')
        self.root.configure(bg = '#AED6F1')
        
        self.login_page()
        
        self.root.mainloop()
        
         
    def login_page(self):
        
        self.clear()
        
        # Heading of login page
        heading = Label(self.root, text ='NLP APPLICATION', bg ='#AED6F1')
        heading.pack(pady=(40, 20))
        heading.configure(font=('tahoma', 30, 'bold'))
        
        # Email
        email = Label(self.root, text ='Email', bg ='#AED6F1')
        email.pack(pady= (10, 10))
        email.configure(font=('tahoma', 12, 'bold'))
        
        # taking email as input and self.email_input use by others
        self.email_input = Entry(self.root, width='40')
        self.email_input.pack(pady=(0,10), ipady=5)
        
        # Password
        email = Label(self.root, text ='Password', bg ='#AED6F1')
        email.pack(pady= (10, 10))
        email.configure(font=('tahoma', 12, 'bold'))
        # taking password as input and self.password_input use by others
        self.password_input = Entry(self.root, width='40', show='*')
        self.password_input.pack(pady=(0,10), ipady=5)
        
        # login Button
        login_btn = Button(self.root, text='Login', width=24, bg='#ff006d')
        login_btn.pack(pady=(30, 10))
        login_btn.configure(font=('tahoma', 10, 'bold'))
        
        # Not a member
        member = Label(self.root, text ='Not a memeber ?', bg ='#AED6F1')
        member.pack(pady= (10, 10))
        member.configure(font=('tahoma', 11, 'bold'))
        
        # Register Button
        register_btn = Button(self.root, text='Register Now', width=24, bg='#45b592', command=self.register_page)
        register_btn.pack(pady=(10, 10))
        register_btn.configure(font=('tahoma', 10, 'bold'))
        
    # Creating register page for register button
    def register_page(self):
        
        self.clear()
        
        # Heading of login page
        heading = Label(self.root, text ='NLP APPLICATION', bg ='#AED6F1')
        heading.pack(pady=(40, 5))
        heading.configure(font=('tahoma', 30, 'bold'))
        # Heading of Register page
        heading = Label(self.root, text ='Registeration Page', bg ='#AED6F1')
        heading.pack(pady=(5, 20))
        heading.configure(font=('tahoma', 15, 'bold'))
        
        # Name
        name = Label(self.root, text ='Name', bg ='#AED6F1')
        name.pack(pady= (10, 10))
        name.configure(font=('tahoma', 12, 'bold'))
        # taking name
        self.name_input = Entry(self.root, width='40')
        self.name_input.pack(pady=(0,10), ipady=5)
        
        # Email
        email = Label(self.root, text ='Email', bg ='#AED6F1')
        email.pack(pady= (10, 10))
        email.configure(font=('tahoma', 12, 'bold'))      
        # taking email as input and self.email_input use by others
        self.email_input = Entry(self.root, width='40')
        self.email_input.pack(pady=(0,10), ipady=5)
        
        # Password
        email = Label(self.root, text ='Password', bg ='#AED6F1')
        email.pack(pady= (10, 10))
        email.configure(font=('tahoma', 12, 'bold'))
        # taking password as input and self.password_input use by others
        self.password_input = Entry(self.root, width='40', show='*')
        self.password_input.pack(pady=(0,10), ipady=5)
        
        # Register Button
        register_btn = Button(self.root, text='Register', width=24, bg='#45b592')
        register_btn.pack(pady=(30, 10))
        register_btn.configure(font=('tahoma', 10, 'bold'))
        
        # Already a member
        member = Label(self.root, text ='Already a memeber ?', bg ='#AED6F1')
        member.pack(pady= (10, 10))
        member.configure(font=('tahoma', 11, 'bold'))
        
        # Login Button
        login_btn = Button(self.root, text='Login Now', width=24, bg='#ff006d', command=self.login_page)
        login_btn.pack(pady=(10, 10))
        login_btn.configure(font=('tahoma', 10, 'bold'))
        
        
    # Utility function thats helps to clear the function for register the page    
    def clear(self):
        # Clear the existing page details after click on register now button
        for i in self.root.pack_slaves():
            i.destroy()
        
    
nlp = NLPApp()
