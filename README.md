# CV_2024_STREAMLIT
repo for personal webpage made with Streamlit

## 4 pages:
- `about me`
- `resume`
- `portfolio`
- `add comments`:
    - this connects to `Google Firebase` where comments are stored using this `pydantic` model:

```py
class Form(BaseModel):
'''a simple validation form

:param _type_ BaseModel: _description_
'''
name: str = Field(description='the name of the user', min_length=1)
email: EmailStr = Field(description='the email of the user')
comment: str | None = Field(default = None, description='the comment left by the user')
time: str = Field(description='the time at which the comment what made')
```