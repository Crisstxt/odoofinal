# -*- coding: utf-8 -*-

from odoo import models, fields, api

class usuario(models.Model):
    _name = 'res.partner'
    _description = 'Usuario'
    _inherit = 'res.partner'    
    
    name = fields.Char(required = True)
    email = fields.Char(required = True)
    contrasenya = fields.Char(required = True)
    image_1920 = fields.Image(max_width = 250, max_height = 250)
    monedero = fields.Float()
    usuario_valoracion = fields.One2many('simarropop.valoracion', 'valoracion_usuario')
    usuario_articulo = fields.One2many('simarropop.articulo', 'user')
    is_user = fields.Boolean()
    

class articulo(models.Model):
    _name = 'simarropop.articulo'
    _description = 'el articulo'

    name = fields.Char()
    precio = fields.Float()
    descripcion = fields.Char()
    articulo_categoria = fields.Many2one('simarropop.categoria')
    imagen = fields.One2many('simarropop.foto', 'imagen_articulo')
    imagen_articulo = fields.Image(max_width = 250, max_height = 250, related='imagen.fotoarticulo') 
    user = fields.Many2one('res.partner')
   
class categoria(models.Model):
    _name = 'simarropop.categoria'
    _description = 'las categorias'

    name = fields.Char()
    icono = fields.Image(max_width = 50, max_height = 50)
    categoria_articulo = fields.One2many('simarropop.articulo', 'articulo_categoria')
    
class foto(models.Model):
    _name = 'simarropop.foto'
    _description = 'las fotos'

    fotoarticulo = fields.Image(max_width = 500, max_height = 500) 
    fotourl = fields.Char()
    imagen_articulo = fields.Many2one('simarropop.articulo')   
    
class valoracion(models.Model):
    _name = 'simarropop.valoracion'
    _description = 'las valoraciones'

    name = fields.Char()
    descripcion = fields.Char()
    estrellas = fields.Selection([('1', "Horrible"), ('2',"Malo"), ('3', "Regular"),('4', "Bueno"),('5', "Fantastico")])
    valoracion_usuario = fields.Many2one('res.partner')


class empleado(models.Model):
    _name = 'simarropop.empleado'
    _description = 'Empleados'   
    
    nombre = fields.Char(required = True)
    dni = fields.Char(required = True)
    email = fields.Char(required = True)
    contra = fields.Char(required = True)

class venta(models.Model):
    _name = 'sale.order'
    _description = 'Ventas'   
    _inherit = 'sale.order'  
    
    cliente = fields.Many2one('res.partner')
    articulo = fields.Many2one('simarropop.articulo')
   
class usuario_wizard(models.TransientModel):
    _name = 'simarropop.usuario_wizard'
    _description = 'Usuario wizard'

    name = fields.Char()
    quantity_articles = fields.Integer(compute = "search_ventas")

    def search_ventas(self):
        for u in self:
            if(len(u.usuario_articulo) > 0 ):
                print(u.usuario_articulo)
                return len(u.usuario_articulo)


    def ventas(self):
        self.name.write({'Articulos del usuario': self.quantity_articles
                         })