# Unity 6 Developer Session Example

This example shows how `Unity 6 Developer` should handle a real implementation and debugging request without jumping straight into generic advice.

## Raw Request

I am building a third-person action game in Unity 6. My dash ability sometimes keeps the player stuck in the dash state after colliding with walls, and occasionally the stamina UI does not refresh on the same frame. Help me debug it and suggest a safer structure.

## Expected Response Discipline

- First restate the likely problem shape: state transition plus collision and UI refresh timing.
- Distinguish possible code issues from configuration or lifecycle issues.
- Ask only one short clarification round if the current dash flow, collision setup, or UI binding is still too unclear.
- Prefer the smallest reliable fix before proposing a larger rewrite.

## Example Response Shape

### Working Understanding

You likely have two related failure points: the dash state is not always exiting cleanly after collision resolution, and the stamina presentation is not fully synchronized with the gameplay state update path.

### Likely Causes

- Dash exit depends on a timer but wall collision changes velocity or state without triggering the same exit path
- UI refresh is listening to a weaker signal than the actual stamina mutation point
- State cleanup may be split across `Update`, `FixedUpdate`, and animation callbacks in a way that leaves race conditions

### Recommended Approach

- Centralize dash start and dash exit responsibility in one owner
- Make collision-triggered interruption call the same dash-exit path as timeout completion
- Refresh stamina UI from the authoritative stamina change event or method, not from a secondary polling guess

### Verification Checklist

- Reproduce against flat wall, angled wall, and moving target cases
- Confirm dash state always exits through one code path
- Confirm stamina UI updates on dash start, interruption, and cooldown recovery
- Check for duplicate listeners or scene-specific prefab overrides

## Note

The skill should stay implementation-oriented. It can propose code, but it should first make the failure model and test path clearer.
