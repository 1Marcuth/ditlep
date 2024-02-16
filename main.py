from ditlep import Ditlep
import decouple

ditlep = Ditlep(
    iv = decouple.config("DITLEP_IV"),
    password = decouple.config("DITLEP_PASSWORD"),
    salt = decouple.config("DITLEP_SALT"),
    dk_len = decouple.config("DITLEP_DK_LEN"),
    count = decouple.config("DITLEP_COUNT")
)

print(ditlep.get_fog_islands())