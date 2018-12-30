.. Cerberus documentation master file, created by
   sphinx-quickstart on Sun Nov 25 18:58:33 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Cerberus
========

Cerberus is a microservice for user authentication and authorisation using
:abbr:`RBAC (Role-Based Access Control)`. Cerberus is provided as a Docker
containerised microservice which can be integrated into any software stack.

Abstract
--------

Cerberus is designed as a self-contained Docker-controlled microservice, with
core code written in Python. The preferred interface with the microservice is
RPC over AMQP, provided by RabbitMQ.

Naming
------

In Greek mythology, Cerberus—or the "hound of Hades"—is a multi-headed dog that
guards the gates of the Underworld. Since the microservice provides user
authentication and authorisation, it seemed fitting.

.. toctree::
   :maxdepth: 2
