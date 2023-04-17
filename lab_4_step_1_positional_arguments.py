import boto3

def translate_text():
    client = boto3.client('translate')
    response = client.translate_text(
        Text='I am learning to code in AWS', 
        SourceLanguageCode='en', 
        TargetLanguageCode='es' 
    )
    print(response) 

def main():
    translate_text()

if __name__=="__main__":
    main()
