import boto3


def get_route53_client():
    """
    It will return route53 client object
    """

    client = boto3.client('route53')

    return client


def get_hosted_zone_ids():
    """
    It will return list of hosted zone id
    """
    pass
