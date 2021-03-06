import random
import smtplib

def write_letter(name_var):
    num = random.randint(1,3)
    with open(f'./letter_templates/letter_{num}.txt', 'r') as template:
        letter = template.read()
        new_letter = letter.replace("[NAME]", name_var)
        return(new_letter)

def send_letter(e_mail, output):
    from_address = ['FROM_EMAIL']
    from_password = ['FROM_PWD']
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=from_address, password=from_password)
    connection.sendmail(from_addr=from_address,
                        to_addrs=e_mail,
                        msg='Subject:Happy Birthday! \n\n' + output)
    connection.quit()
