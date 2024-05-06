FROM python:3.9-alpine

ARG USER=demo
ARG GROUP=demo
ARG UID=1000
ARG GID=1000
ARG PORT=8080
ARG VERSION=
ARG CIRCLE_BUILD_URL=
ARG CIRCLE_SHA1=
ARG CIRCLE_USERNAME=
ARG CIRCLE_BUILD_NUM=

# Set enviroment variable for Flask
ENV PORT=${PORT}

# Set enviroment variable for build JSON
ENV VERSION=${VERSION}
ENV CIRCLE_BUILD_URL=${CIRCLE_BUILD_URL}
ENV CIRCLE_SHA1=${CIRCLE_SHA1}
ENV CIRCLE_USERNAME=${CIRCLE_USERNAME}
ENV CIRCLE_BUILD_NUM=${CIRCLE_BUILD_NUM}

# Expose the server port
EXPOSE ${PORT}

# Update and Upgrade Packages for Alpine
RUN apk -U upgrade

# Copy in requirements file for demo
COPY ./demo /demo

# Add a group and user to not use root
# Then set permissions to the demo files
RUN addgroup --gid ${GID} ${GROUP} \
  && adduser --disabled-password --no-create-home --home "/demo" --uid ${UID} --ingroup ${GROUP} ${USER} \
  && chown -R ${UID}:${GID} /demo

# Set Working Directory
WORKDIR /demo

# Use the production requirements file to install needed Python Packages
# Then delete requirements and tests folder as they are not needed
RUN pip install --no-cache-dir -r requirements/production.txt \
    && rm -rf requirements/ tests/

# Switch to non-root user
USER demo

# Set Python3 as entrypoint
# Using -u for unbuffered ouput
ENTRYPOINT ["python3", "-u"]

# Run the Flask Demo
CMD ["flask_run.py"]