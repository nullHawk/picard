# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScriptEditor(object):
    def setupUi(self, ScriptEditor):
        ScriptEditor.setObjectName("ScriptEditor")
        ScriptEditor.setWindowModality(QtCore.Qt.NonModal)
        ScriptEditor.setEnabled(True)
        ScriptEditor.resize(787, 729)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScriptEditor.sizePolicy().hasHeightForWidth())
        ScriptEditor.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ScriptEditor)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter_between_editor_and_examples = QtWidgets.QSplitter(ScriptEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_between_editor_and_examples.sizePolicy().hasHeightForWidth())
        self.splitter_between_editor_and_examples.setSizePolicy(sizePolicy)
        self.splitter_between_editor_and_examples.setMinimumSize(QtCore.QSize(0, 0))
        self.splitter_between_editor_and_examples.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter_between_editor_and_examples.setOrientation(QtCore.Qt.Vertical)
        self.splitter_between_editor_and_examples.setObjectName("splitter_between_editor_and_examples")
        self.frame_4 = QtWidgets.QFrame(self.splitter_between_editor_and_examples)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 250))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.preset_naming_scripts = QtWidgets.QComboBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_naming_scripts.sizePolicy().hasHeightForWidth())
        self.preset_naming_scripts.setSizePolicy(sizePolicy)
        self.preset_naming_scripts.setMinimumSize(QtCore.QSize(200, 0))
        self.preset_naming_scripts.setObjectName("preset_naming_scripts")
        self.horizontalLayout_2.addWidget(self.preset_naming_scripts)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.frame = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 200))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.splitter_between_editor_and_documentation = QtWidgets.QSplitter(self.frame)
        self.splitter_between_editor_and_documentation.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter_between_editor_and_documentation.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_between_editor_and_documentation.setOpaqueResize(True)
        self.splitter_between_editor_and_documentation.setObjectName("splitter_between_editor_and_documentation")
        self.frame_5 = QtWidgets.QFrame(self.splitter_between_editor_and_documentation)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.file_naming_format = ScriptTextEdit(self.frame_5)
        self.file_naming_format.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.file_naming_format.sizePolicy().hasHeightForWidth())
        self.file_naming_format.setSizePolicy(sizePolicy)
        self.file_naming_format.setMinimumSize(QtCore.QSize(0, 50))
        self.file_naming_format.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.file_naming_format.setTabChangesFocus(False)
        self.file_naming_format.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.file_naming_format.setTabStopWidth(20)
        self.file_naming_format.setAcceptRichText(False)
        self.file_naming_format.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.file_naming_format.setObjectName("file_naming_format")
        self.verticalLayout_2.addWidget(self.file_naming_format)
        self.documentation_frame = QtWidgets.QFrame(self.splitter_between_editor_and_documentation)
        self.documentation_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.documentation_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.documentation_frame.setObjectName("documentation_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.documentation_frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.documentation_frame)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_7.addWidget(self.textBrowser)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scripting_doc_link = QtWidgets.QLabel(self.documentation_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scripting_doc_link.sizePolicy().hasHeightForWidth())
        self.scripting_doc_link.setSizePolicy(sizePolicy)
        self.scripting_doc_link.setMinimumSize(QtCore.QSize(0, 20))
        self.scripting_doc_link.setAlignment(QtCore.Qt.AlignCenter)
        self.scripting_doc_link.setWordWrap(True)
        self.scripting_doc_link.setOpenExternalLinks(True)
        self.scripting_doc_link.setObjectName("scripting_doc_link")
        self.horizontalLayout_3.addWidget(self.scripting_doc_link)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_8.addWidget(self.splitter_between_editor_and_documentation)
        self.verticalLayout_5.addWidget(self.frame)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.file_naming_word_wrap = QtWidgets.QCheckBox(self.frame_4)
        self.file_naming_word_wrap.setObjectName("file_naming_word_wrap")
        self.horizontalLayout_5.addWidget(self.file_naming_word_wrap)
        self.renaming_error = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.renaming_error.sizePolicy().hasHeightForWidth())
        self.renaming_error.setSizePolicy(sizePolicy)
        self.renaming_error.setText("")
        self.renaming_error.setAlignment(QtCore.Qt.AlignCenter)
        self.renaming_error.setObjectName("renaming_error")
        self.horizontalLayout_5.addWidget(self.renaming_error)
        self.show_documentation = QtWidgets.QCheckBox(self.frame_4)
        self.show_documentation.setObjectName("show_documentation")
        self.horizontalLayout_5.addWidget(self.show_documentation)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.example_filename_sample_files_button = QtWidgets.QPushButton(self.frame_4)
        self.example_filename_sample_files_button.setObjectName("example_filename_sample_files_button")
        self.horizontalLayout_4.addWidget(self.example_filename_sample_files_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.import_script = QtWidgets.QPushButton(self.frame_4)
        self.import_script.setObjectName("import_script")
        self.horizontalLayout_4.addWidget(self.import_script)
        self.export_script = QtWidgets.QPushButton(self.frame_4)
        self.export_script.setObjectName("export_script")
        self.horizontalLayout_4.addWidget(self.export_script)
        self.file_naming_editor_save = QtWidgets.QPushButton(self.frame_4)
        self.file_naming_editor_save.setObjectName("file_naming_editor_save")
        self.horizontalLayout_4.addWidget(self.file_naming_editor_save)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.groupBox = QtWidgets.QGroupBox(self.splitter_between_editor_and_examples)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 150))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 400))
        self.groupBox.setBaseSize(QtCore.QSize(0, 150))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_between_before_and_after = QtWidgets.QSplitter(self.groupBox)
        self.splitter_between_before_and_after.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_between_before_and_after.setOpaqueResize(True)
        self.splitter_between_before_and_after.setObjectName("splitter_between_before_and_after")
        self.frame_2 = QtWidgets.QFrame(self.splitter_between_before_and_after)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.example_filename_before_label = QtWidgets.QLabel(self.frame_2)
        self.example_filename_before_label.setObjectName("example_filename_before_label")
        self.verticalLayout_4.addWidget(self.example_filename_before_label)
        self.example_filename_before = QtWidgets.QListWidget(self.frame_2)
        self.example_filename_before.setEditTriggers(QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.example_filename_before.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.example_filename_before.setObjectName("example_filename_before")
        self.verticalLayout_4.addWidget(self.example_filename_before)
        self.frame_3 = QtWidgets.QFrame(self.splitter_between_before_and_after)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.example_filename_after_label = QtWidgets.QLabel(self.frame_3)
        self.example_filename_after_label.setObjectName("example_filename_after_label")
        self.verticalLayout_6.addWidget(self.example_filename_after_label)
        self.example_filename_after = QtWidgets.QListWidget(self.frame_3)
        self.example_filename_after.setEditTriggers(QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.example_filename_after.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.example_filename_after.setObjectName("example_filename_after")
        self.verticalLayout_6.addWidget(self.example_filename_after)
        self.verticalLayout.addWidget(self.splitter_between_before_and_after)
        self.verticalLayout_3.addWidget(self.splitter_between_editor_and_examples)

        self.retranslateUi(ScriptEditor)
        QtCore.QMetaObject.connectSlotsByName(ScriptEditor)

    def retranslateUi(self, ScriptEditor):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_("File naming scripts:"))
        self.preset_naming_scripts.setToolTip(_("Select the file naming script to load into the editor"))
        self.scripting_doc_link.setText(_("Open documentation in browser"))
        self.file_naming_word_wrap.setToolTip(_("Word wrap long lines in the editor"))
        self.file_naming_word_wrap.setText(_("Word wrap script"))
        self.show_documentation.setToolTip(_("Open the scripting documentation in a sidebar"))
        self.show_documentation.setText(_("Show Documentation"))
        self.example_filename_sample_files_button.setToolTip(_("Up to 10 items chosen at random from files selected in the main window"))
        self.example_filename_sample_files_button.setText(_("Reload Examples"))
        self.import_script.setToolTip(_("Import a file to replace the current script"))
        self.import_script.setText(_("Import"))
        self.export_script.setToolTip(_("Export the current script to a file"))
        self.export_script.setText(_("Export"))
        self.file_naming_editor_save.setToolTip(_("Save the current script to the configuration option settings"))
        self.file_naming_editor_save.setText(_("Save"))
        self.groupBox.setTitle(_("Files will be named like this"))
        self.example_filename_before_label.setText(_("Before"))
        self.example_filename_after_label.setText(_("After"))
from picard.ui.widgets.scripttextedit import ScriptTextEdit
