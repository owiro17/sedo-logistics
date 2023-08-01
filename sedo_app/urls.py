from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about_us/',views.about_us,name='about_us'),
    # path('ourservices/',views.ourservices,name='ourservices'),
    # path('login/',views.login,name='login'),
    # path('signup/',views.signup,name='signup'),
    path('contactUs/',views.contactUs,name='contactUs'),
    path('air-freight/',views.air_frieght,name='air-freight'),
    path('rail-freight/',views.rail_frieght,name='rail-freight'),
    path('road-freight/',views.road_frieght,name='road-freight'),
    path('sea-freight/',views.sea_frieght,name='sea-freight'),
    path('cargo-insuarance/',views.cargo_insuarance,name='cargo-insuarance'),
    path('customs-clearance/',views.customs_clearance,name='customs-clearance'),
    path('project-logistics/',views.project_logistics,name='project-logistics'),
    path('warehouse-management/',views.warehouse_management,name='warehouse-management'),
    path('removal/',views.removal,name='remove'),

]
