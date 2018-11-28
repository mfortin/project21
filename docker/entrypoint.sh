#!/bin/sh

export IP=$(hostname)

cd /rtc
node server.js
