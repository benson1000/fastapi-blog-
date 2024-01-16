from pydantic import BaseModel, EmailStr, Field, SecretStr, ValidationError, validator
import re
#properties required during user creation

class UserCreate(BaseModel):
    email : EmailStr
    password : SecretStr
    
    @validator("password")
    def validate_password(cls, value):
        # Ensure at least 1 uppercase, 1 lowercase, 1 numeric, and 1 special character
        if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', value.get_secret_value()):
            raise ValidationError(
                'Password must contain at least 1 uppercase letter, 1 lowercase letter, 1 numeric digit, and 1 special character'
            )
        return value
