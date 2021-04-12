FROM openjdk:8-jdk-alpine
EXPOSE 8080
ADD /target/KubeSpringApp.jar KubeSpringApp.jar
# ARG JAR_FILE=target/*.jar
# COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/KubeSpringApp.jar"]