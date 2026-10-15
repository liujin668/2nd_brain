"""Fail-closed LSF integration contract; deliberately NOT a working backend.

Do not turn this into a shell=True command string. Implement and test site-specific
argv construction, state parsing, durable job ownership and cancellation first.
"""


class LsfAdapter:
    implemented = False

    def submit(self, worker_argv, cwd, log_path, resources, submission_token):
        """Persist intent/token before submission; return {job_id, cluster, token}.

        If submission outcome is uncertain, reconcile by the unique token before
        retrying. A wrapper using bsub -K is insufficient unless it also captures
        job ID early enough to cancel a timeout/interruption. Never infer success
        from the bsub process alone.
        """
        raise NotImplementedError("LSF submission is not integrated")

    def query(self, owned_jobs):
        """Batch-query live/history states; preserve raw status and exit cause.

        PEND/RUN/suspended/UNKWN/DONE/EXIT are scheduler states, not DUT results.
        Missing live job records require history/accounting reconciliation and
        bounded retry. DONE + missing worker result is INCOMPLETE, never PASS.
        """
        raise NotImplementedError("LSF status/history reconciliation is not integrated")

    def cancel(self, owned_job):
        """Cancel only a recorded job owned by this regression; confirm terminal state."""
        raise NotImplementedError("LSF cancellation is not integrated")

    def resume(self, persisted_jobs):
        """Reconcile jobs after controller restart; never resubmit blindly."""
        raise NotImplementedError("LSF recovery is not integrated")
