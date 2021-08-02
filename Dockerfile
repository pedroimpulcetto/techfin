FROM public.ecr.aws/lambda/python:3.8

# Install the function's dependencies 
# Copy file requirements.txt from your project folder and install
# the requirements in the app directory. 

COPY . .
RUN  pip3 install -r requirements.txt

# Copy handler function (from the local app directory)

# Overwrite the command by providing a different command directly in the template.
CMD ["main.handler"]     
        