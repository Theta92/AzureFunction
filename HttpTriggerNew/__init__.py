import os
import logging
import azure.functions as func
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

    
def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')
    

    name = req.params.get('name')
    
    try:
        email=req.params.get("email")
        message=req.params.get("message")
        subject= req.params.get("subject")
        send_with_sendgrid(email,subject,message)
    except Exception as e:
        logging.error("The email request failed")
        send_with_sendgrid(emails=["tooshoba@gmail.com", "nanothman@gmail@gmail.com","bertomerry@gmail.com"],subject="Alert!",message="Something went wrong")
        
    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully.",
             status_code=200

        )    


def send_with_sendgrid(emails,subject,message):
    message = Mail(
        from_email='james@skincarecoal.onmicrosoft.com',
        to_emails=emails,
        subject=subject,
        html_content=message
        )

    sg = SendGridAPIClient("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")
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)
