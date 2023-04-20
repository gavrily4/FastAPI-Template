from pydantic import BaseModel, EmailStr, validator, Field


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str


class LoginModel(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=50)

    @validator("password")
    def hexify_pass(cls, password):
        if not isinstance(password, str):
            raise ValueError('password must be string!')
        password = password.encode('utf-8').hex()
        return password

