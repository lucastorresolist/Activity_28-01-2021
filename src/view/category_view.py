from flask import Flask, render_template, Blueprint, request, redirect

from src.controllers.category_controller import CategoryController
from src.models.category import Category

category_controller = CategoryController()
category_bp = Blueprint('category', __name__)

@category_bp.route('/category')
def category_list():
    categories = CategoryController().read_all()
    return render_template('category.html', categories=categories)


@category_bp.route('/category/create')
def category_form():
    return render_template('category_create.html')


@category_bp.route('/category/created')
def category_create():
    name = request.args.get('name')
    description = request.args.get('description')
    category= Category(name, description)
    category_controller.create(category)

    return redirect('/category')


@category_bp.route('/category/update')
def category_update():
    id_ = request.args.get('id')
    category = category_controller.read_by_id(int(id_))
    
    return render_template('category_create.html', category=category)


@category_bp.route('/category/delete')
def category_delete():
    id_ = request.args.get('id')
    category = category_controller.read_by_id(int(id_))
    category_controller.delete(category)
    
    return redirect('/category')