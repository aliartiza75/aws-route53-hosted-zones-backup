import boto3


def get_route53_client():
    """
    It will return route53 client object
    """

    client = boto3.client('route53')

    return client
