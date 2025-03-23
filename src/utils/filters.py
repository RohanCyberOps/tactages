def filter_by_ip(packets, ip_address):
    """
    Filter packets by IP address.
    """
    return [packet for packet in packets if ip_address in packet]