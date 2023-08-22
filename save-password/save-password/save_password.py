from cat.mad_hatter.decorators import tool, hook
import cryptography
from cryptography.fernet import Fernet

try:
    with open("chiave.txt", "rb") as file_testo:
        chiave = file_testo.read()

    if len(chiave) == 0:
        chiave = Fernet.generate_key()

        with open("chiave.txt", "wb") as file_chiave:
            file_chiave.write(chiave)
except:
    chiave = Fernet.generate_key()

    with open("chiave.txt", "wb") as file_chiave:
        file_chiave.write(chiave)

fernet = Fernet(chiave)


@tool(return_direct=True)
def save_the_password(tool_input, cat):  #
    """A fuction that is used by the user to get the password the password and the context are passed as input, for example server_moncler and Giovanni2023!
    the input will then be separated by - with server_moncler-Giovanni2023!"""
    contesto, password = tool_input.split("-")

    password = password.encode()
    criptato = fernet.encrypt(password)

    with open(contesto + ".txt", "wb") as file_password:
        file_password.write(criptato)

    return "the password is saved correctly"


@tool(return_direct=True)
def get_the_password(tool_input, cat):  #
    """A fuction that is used by the user the save passwordthe context is passed as input, for example server_moncler
    the input will then be separated by - with server_moncler-null"""
    contesto, password = tool_input.split("-")

    try:
        with open(contesto + ".txt", "rb") as file_testo:
            criptato = file_testo.read()

        decriptato = fernet.decrypt(criptato)

        return "the password for " + str(contesto) + ": " + str(decriptato)

    except:
        return (
            "sorry but I could not find the password for "
            + context
            + " try to re-save it"
        )
