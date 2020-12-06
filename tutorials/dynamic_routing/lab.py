from madt_lib.network import Network, Overlay


def main():
    madt = Network('15.0.0.0/8')

    image='quay.io/footloose/centos7:0.6.0'
    #  server = madt.create_node('server', image='madt/nginx')
    server = madt.create_node('server', image=image)
    clients = madt.generate_nodes('client', 6, image=image,
                                  #  entrypoint='sh -c "while true; do wget -O - -T 3 $SERVER; sleep 1; done"')
          entrypoint='sh -c "while true; do touch /testfile ; sleep 1; done"')

    routers = madt.generate_nodes('router', 3)
    madt.create_subnet('subnet1', (routers[0], *clients[:3]))
    madt.create_subnet('subnet2', (routers[1], *clients[3:]))
    madt.create_subnet('subnet3', routers)
    madt.create_subnet('subnet4', (routers[2], server))

    madt.create_overlay(Overlay.RIP, 'RIP', routers)

    madt.configure(verbose=True)
    for client in clients:
        client.add_options(environment={'SERVER': server.get_ip()})
    madt.render('../../labs/dynamic_routing', verbose=True)


if __name__ == "__main__":
    main()

