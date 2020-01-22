from marshmallow import fields, Schema


class BookRequestSchema(Schema):
    requestId = fields.Number(attribute="request_id")
    title = fields.String(attribute="title")
    email = fields.String(attribute="email")
    created_datetime = fields.DateTime(attribute="created_time")
