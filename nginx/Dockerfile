# Image pull
FROM nginx:latest

# Delete exiting nginx configurations from image.
RUN rm /etc/nginx/conf.d/default.conf

# Copying default nginx development configurations.
COPY nginx.conf /etc/nginx/conf.d
