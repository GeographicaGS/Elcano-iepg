Module data.core
================
This are the core objects of the data module.


Time Class
----------
The Time class handles time. It is based on a time lapse with a start and an end. If both are the same, the time lapse is a given time corresponding to the selected time. Maximum time resolution is a second. Time lapse is closed: extremes are included in the lapse. 

Initialization can be very flexible, and is always determined by parsing a string::

   core.Time("2013-01-02 12:23|2014-02-02 13:23") > Time: 2013-01-02 12:23 | 2014-02-02 13:23

   core.Time("2013-01-02|2014-02-02") > Time: 2013-01-02 00:00 | 2014-02-02 00:00

   core.Time("2013-02-01 03:21") > Time: 2013-02-01 03:21:00 | 2013-02-01 03:21:00

   core.Time("2013-01") > Time: 2013-01-15 00:00:00 | 2013-01-15 00:00:00

   core.Time("2013") > Time: 2013-07-01 00:00:00 | 2013-07-01 00:00:00

.. note::
   If end date is smaller than start date, both start and end are finally set to None.


Methods
^^^^^^^

.. autoclass:: data.core.Time
   :members:


GeoVariableArray Class
----------------------
The GeoVariableArray class stores data in a NumPy ndarray for a set of Time, Geoentity, and Variable instances. Data can be retrieved by slicing the inner ndarray, for example::

   geoArray[0,0,0] > gets data for Geoentity 0, Time 0, and Variable 0

   geoArray[(0,3),0,0] > gets data for Geoentity 0 and 3, Time 0, and Variable 0

   geoArray[3:6,0:2,0] > gets data for Geoentity 3 to 6, Time 0 to 2, and Variable 0
   
   geoArray[0,:,:] > gets all data for Geoentity 0, all times and all variables

   geoArray["


Methods
^^^^^^^

.. autoclass:: data.core.GeoVariableArray
   :members: geoentity, time, variable, merge, shape, size, data

