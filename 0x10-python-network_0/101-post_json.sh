#!/bin/bash
# Testing server and request of jason
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
