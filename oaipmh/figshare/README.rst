Records retrieved from OAI-PMH harvest for Figshare can have the following outcomes:

- Create new object in GMN
- Update existing object in GMN
- Result in a log entry that a minor revision was not updated
- Be ignored entirely


Plant UML diagram of logic for processing records:

plant UML::

  @startuml
  start
  :parse SID, PID, date, SciMeta
  from record in OAI-PMH harvest;
  if (SID exists in GMN?) then (yes)
    if (PID exists in GMN?) then (yes)
      if (record date for PID is 
          newer than date in GMN) then (yes)
          : log ignore minor 
            revision event;
      else (no)
          : pass;
      endif
    else (no)
    :MN.update() + 
     log update event;
    endif
  else (no) 
   : MN.create() +
     log create event;
  endif
  stop
  @enduml


asdf
