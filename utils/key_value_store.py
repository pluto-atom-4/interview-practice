class KeyValueStore:
    def __init__(self):
        self.store = {}

    def execute(self, commands):
        results = []
        for cmd in commands:
            parts = cmd.split()
            action = parts[0]

            if action == "PUT":
                self.store[parts[1]] = parts[2]
                results.append("ACCEPTED")
            elif action == "GET":
                results.append(self.store.get(parts[1], "NOT FOUND"))
            elif action == "DELETE":
                if parts[1] in self.store:
                    del self.store[parts[1]]
                    results.append("ACCEPTED")
                else:
                    results.append("NOT FOUND")
        return results


def main() -> None:
    # Usage
    commands = ['PUT a 10', 'GET a', 'DELETE a', 'GET a']
    kv = KeyValueStore()
    print("\n".join(kv.execute(commands)))


if __name__ == "__main__":
    main()