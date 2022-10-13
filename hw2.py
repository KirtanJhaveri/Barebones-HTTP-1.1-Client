# import logging
"""modules for socket and ssl"""
import sys
import socket
import ssl


def retrieve_url(url):
    """
       return bytes of the body of the document at url
    """
    try:
        port = 80
        subdir_index = 0
        response_code = -1
        port_index = 0

        host_index = url.rfind("//")
        subdir_index = url.find("/", host_index + 2, )
        port_index = url.find(":", host_index + 2, )

        if subdir_index > 0 and port_index > 0:
            port = int(url[port_index + 1: subdir_index])
            host = url[host_index + 2: port_index]
            subdir = url[subdir_index:]

        elif subdir_index > 0:
            host = url[host_index + 2: subdir_index]
            subdir = url[subdir_index:]

        else:
            host = url[host_index + 2:]
            subdir = "/"

        clientside = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if url.find("https") >= 0 and subdir_index > 0:
            port = 443
            clientside = ssl.create_default_context().wrap_socket(
                clientside, server_hostname=host)
            clientside.connect((host, port))
        else:
            clientside.connect((host, port))

        message = f"GET {subdir} HTTP/1.1\r\n" \
                  f"Host: {host}:{port}\r\n" \
                  f"User-Agent: python-requests/2.28.1\r\n" \
                  f"Accept: */*\r\n" \
                  f"Connection: close\r\n\r\n"
        clientside.send(message.encode())
        temp_data = clientside.recv(4096)

        data = b""  # change to list because python does weird shit
        while len(temp_data) > 0:
            data = data + temp_data  # append to list
            temp_data = clientside.recv(4096)

        response_code = data.rfind(b"301")
        if response_code >= 0:
            response_code = 0
            redirect = data[data.find(b"Location: ") +
                            10: data.find(b"Host") - 2]
            return retrieve_url(redirect.decode())

        response_code = data.find(b"Transfer-Encoding: chunked\r\n")
        if response_code >= 0:
            header_index = data.split(b"\r\n\r\n", 2)
            data = header_index[1]
            return processing_chunks(data)

        response_code = data.rfind(b"200 OK")
        if response_code == -1:
            return None

        header_index = data.find(b"\r\n\r\n")
        data = data[header_index + 4:]

        return data
    except socket.error:
        return None


def processing_chunks(data):
    """this function handles data if it has chunked transfer encoding"""
    chunked_data = b""
    while True:

        chunk_splits = data.split(b"\r\n", 1)  # Splitting at first \r\n

        hex_size = chunk_splits[0]

        if hex_size == b'0':  # breaks if reaches 0 end of data/packet
            break
        int_size = int(hex_size, 16)

        temp_chunk = chunk_splits[1]
        chunked_data += temp_chunk[:int_size]
        data = temp_chunk[int_size + 2:]

    return chunked_data


if __name__ == "__main__":
    sys.stdout.buffer.write(retrieve_url(sys.argv[1]))
    # pylint: disable=no-member
