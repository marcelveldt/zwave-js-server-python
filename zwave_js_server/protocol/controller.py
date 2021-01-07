"""Provide a protocol for the controller model."""
from enum import Enum
from typing import TYPE_CHECKING

from ..model.node import Node

if TYPE_CHECKING:
    from ..model.controller import Controller, ControllerEvent


class Type(Enum):
    """Represent a controller event type."""

    INCLUSION_FAILED = "inclusion failed"
    EXCLUSION_FAILED = "exclusion failed"
    INCLUSION_STARTED = "inclusion started"
    EXCLUSION_STARTED = "exclusion started"
    INCLUSION_STOPPED = "inclusion stopped"
    EXCLUSION_STOPPED = "exclusion stopped"
    NODE_ADDED = "node added"
    NODE_REMOVED = "node removed"
    HEAL_NETWORK_PROGRESS = "heal network progress"
    HEAL_NETWORK_DONE = "heal network done"


class Handler:
    """Represent an event handler for the controller."""

    @classmethod
    def handle_inclusion_failed(
        cls, controller: "Controller", event: "ControllerEvent"
    ) -> None:
        """Process a inclusion failed event."""

    @classmethod
    def handle_exclusion_failed(
        cls, controller: "Controller", event: "ControllerEvent"
    ) -> None:
        """Process a controller event."""

    @classmethod
    def handle_inclusion_started(
        cls, controller: "Controller", event: "ControllerEvent"
    ) -> None:
        """Process a node event."""

    @classmethod
    def handle_exclusion_started(
        cls, controller: "Controller", event: "ControllerEvent"
    ) -> None:
        """Process a node event."""

    @classmethod
    def handle_inclusion_stopped(
        cls, controller: "Controller", event: "ControllerEvent"
    ) -> None:
        """Process a node event."""

    @classmethod
    def handle_exclusion_stopped(
        cls, controller: "Controller", event: "ControllerEvent"
    ) -> None:
        """Process a node event."""

    @classmethod
    def handle_node_added(
        cls, controller: "Controller", event: "ControllerEvent"
    ) -> None:
        """Process a node event."""
        node = event.data["node"] = Node(event.data["node"])
        controller.nodes[node.node_id] = node

    @classmethod
    def handle_node_removed(
        cls, controller: "Controller", event: "ControllerEvent"
    ) -> None:
        """Process a node event."""
        event.data["node"] = controller.nodes.pop(event.data["node"]["nodeId"])

    @classmethod
    def handle_heal_network_progress(
        cls, controller: "Controller", event: "ControllerEvent"
    ) -> None:
        """Process a node event."""

    @classmethod
    def handle_heal_network_done(
        cls, controller: "Controller", event: "ControllerEvent"
    ) -> None:
        """Process a node event."""