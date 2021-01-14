FROM nginx:1.19.0-alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY --from=build-stage ../dist_volume/ /app/dist