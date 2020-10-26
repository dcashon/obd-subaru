import obd

obd.logger.setLevel(obd.logging.DEBUG)

# this doesnt seem to work with ISO9141-2 protocol
# but is sufficient for GUI testing
connection = obd.OBD(fast=False)

speed = obd.commands.SPEED

test = connection.query(speed)

print(test.value)
