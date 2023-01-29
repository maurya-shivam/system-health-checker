import smtplib as smt
import uuid, datetime, socket, ssl



def connect(smtp_mailaddr, port, from_id, passwd, to_id, message):
    try:
        context = ssl.create_default_context()
        with smt.SMTP_SSL(smtp_mailaddr, port = port, context = context) as connection:
            connection.ehlo()
            connection.login(from_id, passwd)          
            connection.send_message(message)

    except NameError as e:
        print('**Name Error**\nSomething wrong with var. naming:\nDetails are: ',e)
    except ConnectionRefusedError:
        print('The server has refused the connection. Bad connection settings?')
    except smt.SMTPConnectError: 
        print('Failed to connect to the server. Bad connection settings?')
    except smt.SMTPServerDisconnected:
        print('Failed to connect to the server. Wrong user/password?')
    except smt.SMTPException as e:
        print('SMTP error occurred: ', e)
    else:
        print('\n((The message has been send))\n')
    finally:
        print('\nQuitting from the server..............')


if __name__ == "__main__":
    connect()