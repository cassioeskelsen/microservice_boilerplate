# YAMB - Yet Another Microservice Boilerplate

Ramblings about a simple but efficient microservice boilerplate

**Disclaimer**: this boilerplate is tailored for the requirements/environment for the company I work for. 

However, I believe it can help people who are thinking about working with microservices and don't know where to start.

For better understand of the architechture: our company run all containers on AKS (Azure Kubernetes Services ). All microservices
communicates with others through RabbitMQ messages or API. The main database is Mongo and each microservice is responsible for your data.

In practice, some microservices always run together. For example, services that process partner requests. In this case, we have a microservice to receive and initially validate the data (basically schema). The validated data is sent to a worker who effectively processes requests.

So, in this boilerplate I have a directory with an API application and another with the worker. See each of these directories as a separate microservice, I didn't want to separate into 2 repositories in order to keep all the content together.

#### Libraries

[FastAPI](https://github.com/tiangolo/fastapi) - a complete replacement for Flask foccused on API construction. [Why?](https://www.quora.com/What-are-the-advantages-of-using-FastAPI-over-flask)

[uvicorn](http://www.uvicorn.org/) - An ASGI server. [Why ASGI Server?](https://www.maxongzb.com/why-asgi-is-replacing-wsgi-in-django-reading-time-3-mins/)

[UltraJSON](https://github.com/ultrajson/ultrajson) - UltraJSON is an ultra fast JSON encoder and decoder written in pure C



