#!/usr/bin/python3
from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import facade
import re
