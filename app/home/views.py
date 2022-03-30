#-*- coding:utf-8 -*-
# author:Agam
# datetime:2018-11-05

from app.home import home
from flask import render_template
from flask import render_template, make_response, session, redirect, url_for, request, flash, abort


@home.route("/")
def index():
    return redirect(request.args.get("next") or url_for("admin.index"))
