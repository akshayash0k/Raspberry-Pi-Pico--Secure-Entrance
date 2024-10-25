import mfrc522

reader = mfrc522.MFRC522()

def read_tag():
            try:
                id, text = reader.read()
                return id
            except:
                return None           
            
tag_id = read_tag()
if tag_id:
    print("RFID tag detected:", tag_id)
else:
    print("No RFID tag found")