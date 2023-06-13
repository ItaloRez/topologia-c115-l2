from mininet.topo import Topo


class CustomTopology(Topo):
    def __init__(self):

        Topo.__init__(self)
        # Adicionando os switches s1, s2 e s3 à topologia
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Adicionando os hosts h8 e h7 conectados ao switch s1
        h8 = self.addHost('h8')
        h7 = self.addHost('h7')
        self.addLink(h8, s1)
        self.addLink(h7, s1)

        # Adicionando os hosts h1, h2 e h3 conectados ao switch s2
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        self.addLink(h1, s2)
        self.addLink(h2, s2)
        self.addLink(h3, s2)

        # Adicionando os hosts h4, h5 e h6 conectados ao switch s3
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        self.addLink(h4, s3)
        self.addLink(h5, s3)
        self.addLink(h6, s3)

        # Adicionando os switches s1, s2 e s3 conectados entre si
        self.addLink(s1, s2)
        self.addLink(s1, s3)


topos = {'custom': (lambda: CustomTopology())}
