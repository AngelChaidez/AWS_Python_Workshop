import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###

kwargs={
    "Text":"I am learning to code in AWS",
    "TargetLanguageCode":"fr",
    "SourceLanguageCode":"en"
    
    }

def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()
