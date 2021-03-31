#elif "tell me" in query:
            query = query.split(" ")
            location = query[2]+query[3] 
            speak("sir According to google " + location + " is.")
            webbrowser.open("http://www.google.com/search?q="+ location)
        
        #elif "search for" in query:
            query = query.split(" ")
            location =query[2]
            speak("sir According to google " + location + " is.")
            webbrowser.open("http://www.google.com/search?q="+ location)
            
        
        #elif "show me" in query:
            query = query.split(" ")
            location = query[2]+' '+query[3]+' '+query[4]
            speak("sir according to google " + location+"is")
            webbrowser.open("http://www.google.com/search?q="+location)  