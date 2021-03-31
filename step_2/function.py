def read_input():
    return "some input"


def do_calculation(data):
    return data + " " + data


def send_email(body, to):
    # some magic that sends the email
    return False


def main():
    inputValue = read_input()
    result = do_calculation(inputValue)
    sendEmailResult = send_email(result, "dominik.fretz@gmail.com")
    if sendEmailResult == True:
        print("send email successful")
    else:
        print("Send email UNSUCCESSFUL")

    return


main()
