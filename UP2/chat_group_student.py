S_ALONE = 0
S_TALKING = 1

# ==============================================================================
# Group class:
# member fields:
#   - An array of items, each a Member class
#   - A dictionary that keeps who is a chat group
# member functions:
#    - join: first time in
#    - leave: leave the system, and the group
#    - list_me: who is in chatting with me?
#    - list_all: who is in the system, and the chat groups
#    - connect: connect to a peer in a chat group, and become part of the group
#    - disconnect: leave the chat group but stay in the system
# ==============================================================================


class Group:

    def __init__(self):
        self.members = {}
        self.chat_grps = {}
        self.grp_ever = 0

    def join(self, name):
        self.members[name] = S_ALONE
        return

    def is_member(self, name):

        # IMPLEMENTATION
        # ---- start your code ---- #
        try:
            self.members[name]
            return True
        except:
            return False
        # ---- end of your code --- #

    # implement
    def leave(self, name):
        """
        leave the system, and the group
        """
        # IMPLEMENTATION
        # ---- start your code ---- #
        del self.members[name]
        for key, value in self.chat_grps.items():
            if name in value:
                value.remove(name)

        # ---- end of your code --- #
        return None

    def find_group(self, name):
        """
        Auxiliary function internal to the class; return two
        variables: whether "name" is in a group, and if true
        the key to its group
        """

        found = False
        group_key = 0
        # IMPLEMENTATION
        # ---- start your code ---- #
        for key, value in self.chat_grps.items():
            if name in value:
                found = True
                group_key = key
                return found, group_key

        return found, group_key

        # ---- end of your code --- #

    def connect(self, me, peer):
        """
        me is alone, connecting peer.
        if peer is in a group, join it
        otherwise, create a new group with you and your peer
        """
        peer_in_group, group_key = self.find_group(peer)

        # IMPLEMENTATION
        # ---- start your code ---- #
        if peer_in_group:
            self.chat_grps[group_key].append(me)
        else:
            self.grp_ever += 1
            self.chat_grps[self.grp_ever] = [me, peer]

        self.members[me] = S_TALKING

        # ---- end of your code --- #
        return None

    # implement
    def disconnect(self, me):
        """
        find myself in the group, quit, but stay in the system
        """
        # IMPLEMENTATION
        # ---- start your code ---- #
        for key, value in self.chat_grps.items():
            if me in value:
                value.remove(me)
                self.members[me] = S_ALONE
                if len(value) == 1:
                    self.members[value[0]] = S_ALONE
                    del self.chat_grps[key]
                    break

        # ---- end of your code --- #
        return None

    def list_all(self):
        # a simple minded implementation
        full_list = "Users: ------------" + "\n"
        full_list += str(self.members) + "\n"
        full_list += "Groups: -----------" + "\n"
        full_list += str(self.chat_grps) + "\n"
        return full_list

    # implement
    def list_me(self, me):
        """
        return a list, "me" followed by other peers in my group
        """
        my_list = []
        # IMPLEMENTATION
        # ---- start your code ---- #
        for key, value in self.chat_grps.items():
            if me in value:
                value.remove(me)
                my_list = [me] + value

        # ---- end of your code --- #
        return my_list


if __name__ == "__main__":
    g = Group()
    g.join('a')
    g.join('b')
    g.join('c')
    g.join('d')
    print(g.list_all())

    # testing is_member()
    print(g.is_member('a'), g.is_member('s'))

    # testing connect()
    g.connect('c', 'd')
    g.join('s')
    g.connect('s', 'c')
    print(g.list_all())

    # testing find_group()
    print(g.find_group('a'), g.find_group('s'))

    # testing list_me()
    print(g.list_me('s'))

    # testing leave(), disconnect()
    g.leave('c')
    g.disconnect('s')
    print(g.list_all())
