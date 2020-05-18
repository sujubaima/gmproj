Event_1 = \
{
  "name": "Event_1",
  "actions": [{
    "type": "ShowDialog", "dialog": "Dialog_1"
  }]
}

Event_2 = \
{
  "name": "Event_2",
  "actions": [{
     "type": "GetItem", "subject": "Person_0", "item": "Item_1", "quantity": 1
  }, {
     "type": "TriggerOn", "event": "Event_3"
  }]
}

Event_3 = \
{
  "name": "Event_3",
  "actions": [{
    "type": "ShowDialog", "dialog": "Dialog_3"
  }, {
    "type": "TriggerOn", "event": "Event_4"
  }]
}

Event_4 = \
{
  "name": "Event_4",
  "actions": [{
    "type": "ShowDialog", "dialog": "Dialog_4"
  }, {
    "type": "TriggerOn", "event": "Event_5"
  }]
}

Event_5 = \
{
  "name": "Event_5",
  "conditions": [{
    "type": "EventTriggered", "event": "Event_2", "triggered": True
  }],
  "actions": [{
    "type": "ShowDialog", "dialog": "Dialog_5"
  }]
}

Event_6 = \
{
  "name": "Event_6",
  "actions": [{
    "type": "ShowDialog", "dialog": "Dialog_6"
  }, {
    "type": "TriggerOff", "event": "Event_5"
  }]
}

