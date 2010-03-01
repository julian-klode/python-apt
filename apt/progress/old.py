# progress.py - progress reporting classes
#
#  Copyright (c) 2005-2009 Canonical
#
#  Author: Michael Vogt <michael.vogt@ubuntu.com>
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 2 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
#  USA
"""Deprecated progress reporting classes.

This module provides classes for compatibility with python-apt 0.7. They are
completely deprecated and should not be used anymore.
"""


import os
import sys

import apt_pkg
from apt.deprecation import AttributeDeprecatedBy, function_deprecated_by
import warnings
from apt.progress import base, text

__all__ = []


class OpProgress(base.OpProgress):
    """Abstract class to implement reporting on cache opening."""

    subOp = AttributeDeprecatedBy('subop')
    Op = AttributeDeprecatedBy('op')


class OpTextProgress(OpProgress, text.OpProgress):
    """A simple text based cache open reporting class."""


class FetchProgress(object):
    """Report the download/fetching progress."""

    # download status constants
    (dlDone, dlQueued, dlFailed, dlHit, dlIgnored) = range(5)
    dlStatusStr = {dlDone: "Done", dlQueued: "Queued", dlFailed: "Failed",
                     dlHit: "Hit", dlIgnored: "Ignored"}

    def __init__(self):
        self.eta = 0.0
        self.percent = 0.0
        # Make checking easier
        self.currentBytes = 0
        self.currentItems = 0
        self.totalBytes = 0
        self.totalItems = 0
        self.currentCPS = 0
        warnings.warn("FetchProgress() is deprecated.", DeprecationWarning)

    def start(self):
        """Called when the fetching starts."""

    def stop(self):
        """Called when all files have been fetched."""

    def updateStatus(self, uri, descr, short_descr, status):
        """Called when the status of an item changes.

        This happens eg. when the downloads fails or is completed.
        """

    def update_status_full(self, uri, descr, short_descr, status, file_size,
                           partial_size):
        """Called when the status of an item changes.

        This happens eg. when the downloads fails or is completed. This
        version include information on current filesize and partial size
        """

    def pulse(self):
        """Called periodically to update the user interface.

        Return True to continue or False to cancel.
        """
        self.percent = (((self.currentBytes + self.currentItems) * 100.0) /
                        float(self.totalBytes + self.totalItems))
        if self.currentCPS > 0:
            self.eta = ((self.totalBytes - self.currentBytes) /
                        float(self.currentCPS))
        return True

    def pulse_items(self, items):
        """Called periodically to update the user interface.
        This function includes details about the items being fetched
        Return True to continue or False to cancel.

        """
        self.percent = (((self.currentBytes + self.currentItems) * 100.0) /
                        float(self.totalBytes + self.totalItems))
        if self.currentCPS > 0:
            self.eta = ((self.totalBytes - self.currentBytes) /
                        float(self.currentCPS))
        return True

    def mediaChange(self, medium, drive):
        """react to media change events."""


class TextFetchProgress(FetchProgress):
    """ Ready to use progress object for terminal windows """

    def __init__(self):
        FetchProgress.__init__(self)
        self.items = {}

    def updateStatus(self, uri, descr, short_descr, status):
        """Called when the status of an item changes.

        This happens eg. when the downloads fails or is completed.
        """
        if status != self.dlQueued:
            print "\r%s %s" % (self.dlStatusStr[status], descr)
        self.items[uri] = status

    def pulse(self):
        """Called periodically to update the user interface.

        Return True to continue or False to cancel.
        """
        FetchProgress.pulse(self)
        if self.currentCPS > 0:
            s = "[%2.f%%] %sB/s %s" % (self.percent,
                                    apt_pkg.size_to_str(int(self.currentCPS)),
                                    apt_pkg.time_to_str(int(self.eta)))
        else:
            s = "%2.f%% [Working]" % (self.percent)
        print "\r%s" % (s),
        sys.stdout.flush()
        return True

    def stop(self):
        """Called when all files have been fetched."""
        print "\rDone downloading            "

    def mediaChange(self, medium, drive):
        """react to media change events."""
        print ("Media change: please insert the disc labeled "
               "'%s' in the drive '%s' and press enter") % (medium, drive)

        return raw_input() not in ('c', 'C')


class CdromProgress(base.CdromProgress):
    """Report the cdrom add progress.

    This class has been replaced by apt_pkg.CdromProgress.
    """
    _basetype = base.CdromProgress
    askCdromName = function_deprecated_by(_basetype.ask_cdrom_name)
    changeCdrom = function_deprecated_by(_basetype.change_cdrom)
    del _basetype


class DumbInstallProgress(base.InstallProgress):
    """Report the install progress.

    Subclass this class to implement install progress reporting.
    """

    startUpdate = function_deprecated_by(base.InstallProgress.start_update)
    finishUpdate = function_deprecated_by(base.InstallProgress.finish_update)
    updateInterface = function_deprecated_by(
                base.InstallProgress.update_interface)


class InstallProgress(DumbInstallProgress, base.InstallProgress):
    """An InstallProgress that is pretty useful.

    It supports the attributes 'percent' 'status' and callbacks for the dpkg
    errors and conffiles and status changes.
    """

    selectTimeout = AttributeDeprecatedBy('select_timeout')
    statusChange = function_deprecated_by(base.InstallProgress.status_change)
    updateInterface = function_deprecated_by(
        base.InstallProgress.update_interface)
    waitChild = function_deprecated_by(base.InstallProgress.wait_child)


class DpkgInstallProgress(InstallProgress):
    """Progress handler for a local Debian package installation."""

    def run(self, debfile):
        """Start installing the given Debian package."""
        # Deprecated stuff
        self.debfile = debfile
        self.debname = os.path.basename(debfile).split("_")[0]
        return base.InstallProgress(self, debfile)
