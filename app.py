from tkinter import *
from mydb import Database
from tkinter import messagebox
from api import API

class NLPApp():
    
    def __init__(self):
        
        # Creating DB object & it will access all the methods from mydb.py file
        self.db = Database()
        
        # Creating API object & access all methods from api.py file
        self.api = API()
        
        # login page
        self.root = Tk()
        self.root.title('NLP APP')
        self.root.iconbitmap('Resources/favicon.ico')
        self.root.geometry('480x620')
        self.root.configure(bg = '#AED6F1')
        
        self.login_page()
        
        self.root.mainloop()
        
 #######################################################################################################  
         
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
        login_btn = Button(self.root, text='Login', width=24, bg='#ff006d', command=self.login)
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
       
####################################################################################################### 
  
    # Creating register page for register button
    def register_page(self):
        
        self.clear()
        
        # Heading of login page
        heading1 = Label(self.root, text ='NLP APPLICATION', bg ='#AED6F1')
        heading1.pack(pady=(40, 5))
        heading1.configure(font=('tahoma', 30, 'bold'))
    
        heading2 = Label(self.root, text ='Registeration Page', bg ='#AED6F1')
        heading2.pack(pady=(5, 20))
        heading2.configure(font=('tahoma', 15, 'bold'))
        
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
        register_btn = Button(self.root, text='Register', width=24, bg='#45b592', command=self.registration)
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
        
        
#######################################################################################################  

        
    # Utility function thats helps to clear the function for register the page    
    def clear(self):
        # Clear the existing page details after click on register now button
        for i in self.root.pack_slaves():
            i.destroy()
    
    
 #######################################################################################################     
            
    # Registrastion method after click on Register button
    def registration(self):
        
        # Fetch details form registr page
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        
        response = self.db.add_data(name, email, password)
        if response:
            messagebox.showinfo('Successful', 'Registration Successful ! You can login now')
        else:
            messagebox.showerror('Error', 'Email already exists !')
            
    
#######################################################################################################      
            
    # Login method after click on Login button
    def login(self):
        
        # Check details of login page (valid or not)
        email = self.email_input.get()
        password = self.password_input.get()
        
        response = self.db.search(email, password)
        if response:
            messagebox.showinfo('Successful', 'Login Successful !')
            self.dashboard()
        else:
            messagebox.showerror('Error', 'Try again ! , Incorrect email / password ! ')
   
#######################################################################################################           
    
    def dashboard(self):
        
        self.clear()
        
        # Heading of dashboard
        heading1 = Label(self.root, text ='NLP APPLICATION', bg ='#AED6F1')
        heading1.pack(pady=(40, 5))
        heading1.configure(font=('tahoma', 30, 'bold'))
        heading2 = Label(self.root, text ='Dashboard', bg ='#AED6F1')
        heading2.pack(pady=(5, 20))
        heading2.configure(font=('tahoma', 18, 'bold'))
        
        # Sentiment Button
        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=24, height=2, bg='#45b592', command=self.sentiment)
        sentiment_btn.pack(pady=(30, 10))
        sentiment_btn.configure(font=('tahoma', 13, 'bold'))
        
        # NER Button
        ner_btn = Button(self.root, text='Name Entity Recognition', width=24, height=2, bg='#45b592', command=self.ner)
        ner_btn.pack(pady=(30, 10))
        ner_btn.configure(font=('tahoma', 13, 'bold'))
        
        # Emotion Button
        emotion_btn = Button(self.root, text='Emotion Prediction', width=24, height=2, bg='#45b592', command=self.emotion)
        emotion_btn.pack(pady=(30, 10))
        emotion_btn.configure(font=('tahoma', 13, 'bold'))
        
        # Logout button
        logout_btn = Button(self.root, text='Logout', width=24, bg='#ff006d', command=self.login_page)
        logout_btn.pack(pady=(30, 10))
        logout_btn.configure(font=('tahoma', 11, 'bold'))
   
  #######################################################################################################   
      
    # Sentiment Anaylsis 
    def sentiment(self):
        
        self.clear()
        
        # Heading of sentiment analysis
        heading = Label(self.root, text ='NLP APPLICATION', bg ='#AED6F1')
        heading.pack(pady=(40, 5))
        heading.configure(font=('tahoma', 30, 'bold'))
        
        heading1 = Label(self.root, text ='Sentiment Analysis', bg ='#AED6F1')
        heading1.pack(pady=(5, 20))
        heading1.configure(font=('tahoma', 20, 'bold'))
        
        # Text label for analysis
        text = Label(self.root, text ='Enter the Text :', bg ='#AED6F1')
        text.pack(pady= (10, 10))
        text.configure(font=('tahoma', 9, 'bold'))
        
        # Entry of text
        self.sentiment_input = Entry(self.root, width='40')
        self.sentiment_input.pack(pady=(0,10), ipady=5)
        
        # Sentiment button
        sentiment_btn = Button(self.root, text='Analyze Sentiment', width=24, bg='#ff006d', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(30, 10))
        sentiment_btn.configure(font=('tahoma', 9, 'bold'))
        
        # Sentiment Result
        self.sentiment_result = Label(self.root, text ='', bg ='#AED6F1')
        self.sentiment_result.pack(pady= (10, 10))
        self.sentiment_result.configure(font=('tahoma', 9, 'bold'))
        
        # Goback button
        goback_btn = Button(self.root, text='Go Back', width=24, bg='#00cc66', command=self.dashboard)
        goback_btn.pack(pady=(30, 10))
        goback_btn.configure(font=('tahoma', 9, 'bold'))
        
        
    def do_sentiment_analysis(self):
        
        text = self.sentiment_input.get()
        result = self.api.sentiment_analysis(text)
        
        # Display the analyze text in sentiment result
        txt = ''
        for i in result['sentiment']:
            txt = txt + i + ' : ' + str(result['sentiment'][i]) + '\n'
            #print(i, result['sentiment'],[i])
        
        self.sentiment_result['text'] = txt
        
#######################################################################################################  
   
    def ner(self):
        
        self.clear()
        
        # Heading of NER
        heading = Label(self.root, text ='NLP APPLICATION', bg ='#AED6F1')
        heading.pack(pady=(40, 5))
        heading.configure(font=('tahoma', 30, 'bold'))
        
        heading1 = Label(self.root, text ='Name Entity Recognition', bg ='#AED6F1')
        heading1.pack(pady=(5, 20))
        heading1.configure(font=('tahoma', 20, 'bold'))
        
        # Text label for ner
        text = Label(self.root, text ='Enter the Text', bg ='#AED6F1')
        text.pack(pady= (10, 10))
        text.configure(font=('tahoma', 9, 'bold'))
        
        # Entry of text
        self.ner_input = Entry(self.root, width='40')
        self.ner_input.pack(pady=(0,10), ipady=5)
        
        # NER button
        ner_btn = Button(self.root, text='Analyze Sentiment', width=24, bg='#ff006d', command=self.do_ner)
        ner_btn.pack(pady=(30, 10))
        ner_btn.configure(font=('tahoma', 9, 'bold'))
        
        # NER Result
        self.ner_result = Label(self.root, text ='', bg ='#AED6F1')
        self.ner_result.pack(pady= (10, 10))
        self.ner_result.configure(font=('tahoma', 9, 'bold'))
        
        # Goback button
        goback_btn = Button(self.root, text='Go Back', width=24, bg='#00cc66', command=self.dashboard)
        goback_btn.pack(pady=(30, 10))
        goback_btn.configure(font=('tahoma', 9, 'bold'))
        
    def do_ner(self):
        text = self.ner_input.get()
        result = self.api.name_entity_recognition(text)

        # Display the analyze text in the emotion result
        txt = ''
        for entity in result['entities']:
            name = entity['name']
            category = entity['category']
            confidence_score = round(entity['confidence_score'], 3)
            txt = txt + '{} : {} (Confidence : {})\n'.format(category, name, confidence_score)
        
        self.ner_result['text'] = txt


 #######################################################################################################   
    
    def emotion(self):
        
        self.clear()
        
        # Heading of NER
        heading = Label(self.root, text ='NLP APPLICATION', bg ='#AED6F1')
        heading.pack(pady=(40, 5))
        heading.configure(font=('tahoma', 30, 'bold'))
        
        heading1 = Label(self.root, text ='Emotion Analysis', bg ='#AED6F1')
        heading1.pack(pady=(5, 20))
        heading1.configure(font=('tahoma', 20, 'bold'))
        
        # Text label for ner
        text = Label(self.root, text ='Enter the Text', bg ='#AED6F1')
        text.pack(pady= (10, 10))
        text.configure(font=('tahoma', 9, 'bold'))
        
        # Entry of text
        self.emotion_input = Entry(self.root, width='40')
        self.emotion_input.pack(pady=(0,10), ipady=5)
        
        # Emotion button
        emotion_btn = Button(self.root, text='Analyze Emotion', width=24, bg='#ff006d', command=self.do_emotion_analysis)
        emotion_btn.pack(pady=(30, 10))
        emotion_btn.configure(font=('tahoma', 9, 'bold'))
        
        # Emotion Result
        self.emotion_result = Label(self.root, text ='', bg ='#AED6F1')
        self.emotion_result.pack(pady= (10, 10))
        self.emotion_result.configure(font=('tahoma', 9, 'bold'))
        
        # Goback button
        goback_btn = Button(self.root, text='Go Back', width=24, bg='#00cc66', command=self.dashboard)
        goback_btn.pack(pady=(30, 10))
        goback_btn.configure(font=('tahoma', 9, 'bold'))
    
    
    def do_emotion_analysis(self):
        
        text = self.emotion_input.get()
        result = self.api.emotion_analysis(text)
        
        # Display the analyze text in emotion result
        txt = ''
        for i in result['emotion']:
            txt = txt + i + ' : ' + str(result['emotion'][i]) + '\n'
        self.emotion_result['text'] = txt
    
        
nlp = NLPApp()
